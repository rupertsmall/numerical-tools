% value of function based on a local linear fit of "numpoints" neighbouring points in each direction

function [x,y]=neighboursmooth(xarray,yarray,numpoints)
x=zeros(1,length(xarray));y=zeros(1,length(xarray));
len=length(xarray);
for i=1:len
    bottom=max(1,i-numpoints);
    top=min(len,i+numpoints);
    xsec=xarray(bottom:top);
    ysec=yarray(bottom:top);
    poly=polyfit(xsec,ysec,1);
    x(i)=xarray(i);
    y(i)=poly(1)*x(i)+poly(2);
end


%EOF
