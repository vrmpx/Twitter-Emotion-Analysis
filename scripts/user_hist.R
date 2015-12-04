users <- read.table("~/Workspace/AffectiveComputing/data/users.counts", quote="\"")
names(users) <- c("counts", "uid")

breaks <- c(1:5, 10, 50, 100,500, 1000,2000, 5000, 10000, 30000)
ggplot(users, aes(x = counts)) + geom_histogram(colour="darkblue", size=1, fill="blue", binwidth = .05) + scale_x_log10(breaks = breaks)
