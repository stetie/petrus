library(lattice)
setwd("/home/pi/petrus/data")
files=list.files(pattern="*.csv")
x = do.call("rbind", lapply(files, function(x) read.csv(x)))
#x <- read.csv("data_test/04-04-2015.csv")
x$date <- ISOdate(x$Year, x$Month, x$Day, x$Hour, x$Minute, 0)
month <- c("Jan", "Feb", "Mrz", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez")
x$month <- factor(month[x$Month], levels=month)

#png(filename="graph/04-04-2015.png", width = 800, height = 600, pointsize = 8, bg = 'white', res = 300)
png(filename="/home/pi/petrus/graph/monthly.png")
#pdf()
#today = Sys.time()
#yesterday=today
#yesterday$mday <- yesterday$mday - 1
temp.means <- aggregate(x["Temperature"], x["Month"], mean)
xyplot(Temperature ~ Month, data=temp.means, type="b", xlab="Monate", ylab="Temperatur (°C)", scales=list(x=list(at=1:length(month), lab=month)))
dev.off()
