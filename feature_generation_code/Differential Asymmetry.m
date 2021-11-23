subject = {'s01.mat','s02.mat','s03.mat','s04.mat','s05.mat','s06.mat','s07.mat','s08.mat','s09.mat','s10.mat','s11.mat','s12.mat','s13.mat','s14.mat','s15.mat','s16.mat','s17.mat','s18.mat','s19.mat','s20.mat','s21.mat','s22.mat','s23.mat','s24.mat','s25.mat','s26.mat','s27.mat','s28.mat','s29.mat','s30.mat','s31.mat','s32.mat' };


pair1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14];
pair2 = [17,18,20,21,22,23,25,26,27,28,29,30,31,32];

b1 = [1,4,8,14,31];
b2 = [3,7,13,30,50];



Fs = 128;
Fd = [];
for idx = 1:32
    load(subject{idx},'data')
    disp("Subject " + string(idx))
    
    for num = 1:40
        channel = data(num,:,:);
        channel = reshape(channel,40,8064);
        F = [];
        for band=1:5
           
            for bp = 1:14
                x = channel(pair1(bp),:);
                y = channel(pair2(bp),:);
                [Pxx1,F1] = periodogram(x,rectwin(length(x)),length(x),Fs);
                [Pxx2,F2] = periodogram(y,rectwin(length(y)),length(y),Fs);
                p = abs(bandpower(Pxx1 , F1 , [b1(band) b2(band)] , 'psd') - bandpower(Pxx2 , F2 , [b1(band) b2(band)] , 'psd') );
                F = [F , p ];
            end
            
        end
        Fd = [Fd ;F];    
    end
        
end


