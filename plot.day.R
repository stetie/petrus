library(lattice)
setwd("/home/pi/petrus/data")
files=list.files(pattern="*.csv")
x = do.call("rbind", lapply(files, function(x) read.csv(x)))
#x <- read.csv("data_test/04-04-2015.csv")
x$date <- ISOdate(x$Year, x$Month, x$Day, x$Hour, x$Minute, 0)
#png(filename="graph/04-04-2015.png", width = 800, height = 600, pointsize = 8, bg = 'white', res = 300)
png(filename="graph/last24.png")
#pdf()
today = Sys.time()
yesterday=today
yesterday$mday <- yesterday$mday - 1
xyplot(Temperature ~ date, data=x, type="b", xlab="Zeit", ylab="Temperatur (°C)", subset=date > yesterday)
dev.off()
