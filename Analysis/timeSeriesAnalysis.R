library(reshape)
library(scales)
library(ggplot2)
library(xts)

results <- read.csv("~/Workspace/AffectiveComputing/data/CountrySeries/results.csv", stringsAsFactors = FALSE)

#Convert time to POSIXlt
results$date <- strptime(results$date, format = "%m/%d/%y %H:%M")

#Split into before and after crash
results <- results[results$date < as.POSIXct("09/01/14 00:00", format = "%m/%d/%y %H:%M"),  ]

df.xts <- xts(x = results[, c(2:5)], order.by = results[, "date"])
head(df.xts)

Mode <- function (x){
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

#daily averages
daily.AVG <- apply.daily(df.xts, function(x) apply(x, 2, mean))
daily.mode <- apply.daily(df.xts, function(x) apply(x, 2, Mode))
daily.median <- apply.daily(df.xts, function(x) apply(x, 2, median))
daily.max <- apply.daily(df.xts, function(x) apply(x, 2, max))
daily.min <- apply.daily(df.xts, function(x) apply(x, 2, min))

#rename cols
names(daily.AVG) <- c("us_valence.avg", "us_arousal.avg", "mx_valence.avg", "mx_arousal.avg")
names(daily.mode) <- c("us_valence.mode", "us_arousal.mode", "mx_valence.mode", "mx_arousal.mode")
names(daily.median) <- c("us_valence.median", "us_arousal.median", "mx_valence.median", "mx_arousal.median")
names(daily.max) <- c("us_valence.max", "us_arousal.max", "mx_valence.max", "mx_arousal.max")
names(daily.min) <- c("us_valence.min", "us_arousal.min", "mx_valence.min", "mx_arousal.min")


#Day df
Day <- data.frame(datetime = index(daily.AVG),
                  daily.AVG[, c(1:4)],
                  daily.max[, c(1:4)],
                  daily.min[, c(1:4)], row.names = NULL)

df <- melt(Day[, c("datetime", "us_valence.avg", "mx_valence.avg")], id.vars = "datetime")

ggplot(df, aes(x = datetime, y = value, colour = variable, fill = variable)) + geom_line()


#Lag analysis
withLag <- ccf(Day$us_valence.avg, Day$mx_valence.avg, lag.max = 30, plot = FALSE)
plot(withLag, main="Daily country's mean valence correlation with lag")
withLag$lag[which.max(abs(withLag$acf))]
max(abs(withLag$acf))



#monthly averages
monthly.AVG <- apply.monthly(df.xts, function(x) apply(x, 2, mean))

#rename cols
names(monthly.AVG) <- c("us_valence.avg", "us_arousal.avg", "mx_valence.avg", "mx_arousal.avg")

#Month df
Month <- data.frame(datetime = index(monthly.AVG),
                    monthly.AVG[, c(1:4)],
                    row.names = NULL)

df <- melt(Month[, c("datetime", "us_valence.avg", "mx_valence.avg")], id.vars = "datetime")

ggplot(df, aes(x = datetime, y = value, colour = variable, fill = variable)) + geom_line()


#Lag analysis
withLag <- ccf(Month$us_valence.avg, Month$mx_valence.avg, lag.max = 12, plot = FALSE)
plot(withLag, main="Monthly country's mean valence correlation with lag")
withLag$lag[which.max(abs(withLag$acf))]
max(abs(withLag$acf))


