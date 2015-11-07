emotions_EN <- read.table("~/Workspace/AffectiveComputing/data/EmotionSeries/emotions_EN.counts", quote="\"")
emotions_ES <- read.table("~/Workspace/AffectiveComputing/data/EmotionSeries/emotions_ES.counts", quote="\"")
names(emotions_ES) <- c("counts", "n")
names(emotions_EN) <- c("counts", "n")
emotions_ES$lang <- "es"
emotions_EN$lang <- "en"
emotions_ES$counts <- scale(emotions_ES$counts, center = F, scale= T)
emotions_EN$counts <- scale(emotions_EN$counts, center = F, scale = T)
df <- data.frame(rbind(emotions_ES, emotions_EN))
df$n <- as.factor(df$n)
ggplot(df, aes(x = n, y = counts, group=lang, fill = lang)) + geom_bar(colour="black", stat="identity")
ggplot(df, aes(x = as.integer(n), y = counts, group = lang, colour=lang)) + geom_line() + geom_point() + scale_x_log10() + scale_y_log10()
