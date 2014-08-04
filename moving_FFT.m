% moving FFT algorithm

function [graphs,domain,mFF]=moving_FFT(t_vals,y_vals,sample_rate,FFT_WINDOW)

%linear interpolation
time_step = 1/sample_rate;
tt=min(t_vals):time_step:max(t_vals);
yy=interp1(t_vals,y_vals,tt);

if (FFT_WINDOW < max(t_vals) - min(t_vals))
    %moving fast fourier transform (mFFT)
    N = sample_rate*FFT_WINDOW;                 %number of samples in a section
    iterations = floor(length(tt)/N);           %number of iterations-1 to make of the FFT <=> 'moving' FFT (ie total_iterations = iterations + 1)
    graphs = iterations + 1;                    %number of graphs/windows == number of columns in X, Y
    F = zeros(N-1, iterations + 1);             %the '+1' is for the last iteration that "doesn't fit" into the domain
                                                %the '-1' is for the F(1)=[]
                                                % (see below)
    for index=1:iterations
        section_yy = yy((index-1)*N + 1:index*N);
        FF = 2*fft(section_yy,N)/(N-1);         %take fft and normalize half-plane. store in columns of F
        FF(1) = [];                             %remove. contains irrelevant information
        FF = fftshift(abs(FF));                 %make real values and shift to zero midpoint
        F(1:end,index) = FF;                    %store in columns of matrix F
    end

    %FFT the section that couldn't fit
    section_yy = yy(end - N + 1:end);
    FF = 2*fft(section_yy,N)/(N-1);
    FF(1) = [];
    FF = fftshift(abs(FF));
    F(1:end,end) = FF;
    mFF = F;

elseif (FFT_WINDOW == max(t_vals) - min(t_vals))
    %stationary fast fourier transform (FFT)
    N = sample_rate*FFT_WINDOW;                 %number of samples in a section
    graphs = 1;
    FF = 2*fft(yy,N)/(N-1);
    FF(1) = [];
    FF = fftshift(abs(FF));
    mFF = FF;

else
    graphs = 0; mFF = 0;                        %error
end

%transform domain to frequency (in 1/kyr)
    lenF = N-1;
    if (mod(lenF,2) == 0)                       %is symmetric so in theory should always be odd (due to zero point as well)
    domain = -lenF/2:lenF/2 - 1;
    else
        domain = -(lenF-1)/2:(lenF-1)/2;
    end

    %rescale domain as a frequency axis
    domain = domain*sample_rate/N;

%EOF
