% top hat timeshift. apply a top hat time lag between two
% data sets. do not (!) discard the values that are 'leapfrogged' by values
% in the bulk of the hat. this is a *literal tophat timeshift* NOT a
% physical one so there is cross pollination in time. the time shift is
% bringing the first data set up towards the second (so for paleo dates
% back in time since "bigger" is further into the past).

%top hat == shift for a<x<b and zero outside
%d18O = benthic oxygen measurement

function [time_out,oxb_out,oxw_out]=th_timeshift(time,d18Ob,d18Ow,a,b,shift)
%1. perform the cut
cut_time = min(time)+shift;
time_cut=time(time >= cut_time);
d18Ob_cut=d18Ob(time >= cut_time);
d18Ow_cut=d18Ow(time >= cut_time);

%2. identify the patches (and gaps)
patches = d18Ob_cut >= a & d18Ob_cut <= b;
gaps = ~patches;
lenp=length(patches);
patch_arr_temp=zeros(lenp,2);       %to hold index_beginning,index_end

%note - the index of the beginning may be the same as the index of the end
%of a patch. hence must use ifs and not elseifs
for i=1:lenp
    if i == 1 && patches(i) == 1    %a patch starts immediately
        patch_arr_temp(i,1) = i;
    end
    if patches(i) == 1 && i~=1 && patches(i-1) == 0 %prevent from trying to access patches(0)
        patch_arr_temp(i,1) = i;
    end
    if i==lenp && patches(i) == 1   %a patch ends at the final index
        patch_arr_temp(i,2) = i;
    end
    if patches(i) == 1 && i ~= lenp && patches(i+1) == 0    %prevent from trying to access patches(end+1)
        patch_arr_temp(i,2) = i;
    end
end

%take out zeros/unassigned spaces
p1=patch_arr_temp(:,1);
p1=p1(p1 > 0);
p2=patch_arr_temp(:,2);
p2=p2(p2 > 0);


maxrownonzero=length(p1);
%resize now that we know how many patches there are
patch_arr=zeros(maxrownonzero,4);       %to hold index_beginning,index_end,min_time,max_time of patch
patch_arr(:,1)=p1(1:maxrownonzero);
patch_arr(:,2)=p2(1:maxrownonzero);

%3 min() and max() time for each patch
for i=1:maxrownonzero
    time_patch = time_cut(patch_arr(i,1):patch_arr(i,2));
    patch_arr(i,3)=min(time_patch);
    patch_arr(i,4)=max(time_patch);
end

%2. shift each patch
patch_arr(:,3)=patch_arr(:,3)-shift;
patch_arr(:,4)=patch_arr(:,4)-shift;

%4. sample d18Ow in shifted domains
samples=zeros(1,lenp);        %max possible size. shrink later
samples_index=1;
for i=1:maxrownonzero
    sample_points=(patch_arr(i,2)-patch_arr(i,1)+1);
    step_size=((patch_arr(i,4)-patch_arr(i,3))/sample_points);
    if step_size ~= 0
        time_patch=patch_arr(i,3)+.5*step_size:step_size:patch_arr(i,4);    %sample at midpoints
        samples(1,samples_index:samples_index+length(time_patch)-1)=interp1(time,d18Ow,time_patch);
        samples_index=samples_index+length(time_patch);
    else
        time_value=patch_arr(i,3);
        samples(1,samples_index)=interp1(time,d18Ow,time_value);
        samples_index=samples_index + 1;
    end
end


shifted=samples(samples ~= 0);  %take out the excess zeros (are assuming no values are exactly zero)
shifted_time_section = time_cut(patches);

%5. sample d18Ow in plane/non-shifted domains
non_shifted = d18Ow_cut(gaps);
non_shifted_time_section = time_cut(gaps);

%6. piece it all together
oxb_out=d18Ob_cut;
all_time=sort([shifted_time_section' non_shifted_time_section']);
[sorted order]=sort(all_time);
time_out=time_cut;
oxw_all=[shifted non_shifted];
%sprintf('size shifted == %d %d',size(shifted)) % -- check -- %
oxw_out=oxw_all(order);

end

%EOF
