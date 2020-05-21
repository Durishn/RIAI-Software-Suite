library(MASS)
df<-read.csv("/Users/nicdurish/Desktop/Book1.csv")
summary(df)

#Perform Normality Tests and Transformations on criterion variables
shapiro.test(df$DLMean[1:5000])
yjDL <-yeojohnson(df$DLMean)

shapiro.test(df$ULMean[1:5000])
yjUL <-yeojohnson(df$ULMean)

shapiro.test(df$RTTMean[1:5000])
yjRTT <-yeojohnson(df$RTTMean)


#Day of Week Linear modelling and re evaluating reference
DOWs <- relevel(df$Day.of.Week, ref="Sunday")
DOWw <- relevel(df$Day.of.Week, ref="Wednesday")
#DL
summary(lm(df$DLMean^4.9~DOWs))
summary(lm(df$DLMean^4.9~DOWw))
#UL
summary(lm(df$ULMean^4.9~DOWs))
summary(lm(df$ULMean^4.9~DOWw))
#RTT
summary(lm(df$RTTMean^3.86~DOWs))
summary(lm(df$RTTMean^3.86~DOWw))

#Hour of Day Linear modelling and re evaluating reference
HOD1x <- relevel(df$Time, ref="6:00 AM")
HOD2x <- relevel(df$Time, ref="12:00 PM")
HOD3x <- relevel(df$Time, ref="6:00 PM")
HOD4x <- relevel(df$Time, ref="12:00 AM")
#DL
summary(lm(df$DLMean^4.9~HOD1x))
summary(lm(df$DLMean^4.9~HOD2x))
summary(lm(df$DLMean^4.9~HOD3x))
summary(lm(df$DLMean^4.9~HOD4x))
#UL
summary(lm(df$ULMean^4.9~HOD1x))
summary(lm(df$ULMean^4.9~HOD2x))
summary(lm(df$ULMean^4.9~HOD3x))
summary(lm(df$ULMean^4.9~HOD4x))
#RTT
summary(lm(df$RTTMean^3.86~HOD1x))
summary(lm(df$RTTMean^3.86~HOD2x))
summary(lm(df$RTTMean^3.86~HOD3x))
summary(lm(df$RTTMean^3.86~HOD4x))



#TEMP
summary(df$Estimated.Temp...C.)
sd(df$Estimated.Temp...C.)
#DL
plot(df$Estimated.Temp...C., df$DLMean^4.9 )
summary(lm(df$DLMean^4.9~df$Estimated.Temp...C., ))
abline(5.18435, 0.06354)
#UL
summary(lm(df$ULMean^4.9~df$Estimated.Temp...C., ))
#RTT
summary(lm(df$RTTMean^3.86~df$Estimated.Temp...C., ))

#Hum
summary(df$Estimated.Hum....)
sd(df$Estimated.Hum....)
plot(df$Estimated.Hum...., df$ULMean^4.9 )
summary(lm(df$DLMean^4.9~df$Estimated.Hum....))
abline(5.814e-02, -1.420e-04)
#UL
summary(lm(df$ULMean^4.9~df$Estimated.Hum....))
#RTT
summary(lm(df$RTTMean^3.86~df$Estimated.Hum....))

#Wind Spd
summary(df$Estimated.Wind.Spd..km.h.)
sd(df$Estimated.Wind.Spd..km.h.)
plot(df$Estimated.Wind.Spd..km.h., df$DLMean^4.9 )
summary(lm(df$DLMean^4.9~df$Estimated.Wind.Spd..km.h.))
abline(5.56526, -0.004465)
#UL
summary(lm(df$ULMean^4.9~df$Estimated.Wind.Spd..km.h.))
#RTT
summary(lm(df$RTTMean^3.86~df$Estimated.Wind.Spd..km.h.))



