% moving average using the last and future N points in the domain

function [domain,average]=moving_av(domain_in,range_in,N)
lend=length(domain_in);
domain=domain_in;
average=zeros(1,lend);

for i=1:lend
    top=min(lend,i+N);
    bottom=max(1,i-N);
    average(i)=mean(range_in(bottom:top));
end

end

% EOF
