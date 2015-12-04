library(reshape)
library(scales)
library(ggplot2)
library(xts)

ObamaTweets_valence_arousal <- read.delim("~/Workspace/AffectiveComputing/demo/ObamaTweets_Emotion.tsv", header=FALSE, stringsAsFactors=FALSE)
names(ObamaTweets_valence_arousal) <- c("tid", "uid", "date", "valence", "arousal")


#Convert time to POSIXlt
ObamaTweets_valence_arousal$date <- strptime(ObamaTweets_valence_arousal$date, format = "%Y-%m-%d %H:%M:%S")

df.xts <- xts(x = ObamaTweets_valence_arousal[, c(4:5)], order.by = ObamaTweets_valence_arousal[, "date"])
head(df.xts)
daily.AVG <- apply.daily(df.xts, function(x) apply(x, 2, mean))
names(daily.AVG) <- c("valence.avg", "arousal.avg")

Day <- data.frame(datetime = index(daily.AVG),
                  daily.AVG[, c(1:2)],
                  row.names = NULL)

df <- melt(Day[, c("datetime", "valence.avg", "arousal.avg")], id.vars = "datetime")

ggplot(df, aes(x = datetime, y = value, colour = variable, fill = variable)) + geom_point() + geom_line() + ggtitle("Emotion in Obama's Tweets")
