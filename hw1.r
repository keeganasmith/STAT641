df <- read.csv("data.csv",
                header = TRUE, sep = ",")
head(df)

fert_A_df = df[df$Fertilizer == "A", ] 
print("fert A mean height: ")
mean(fert_A_df[["Height_cm"]])
print("fert A mean tomatoes: ")
mean(fert_A_df[["Number_of_Tomatoes"]])

fert_B_df = df[df$Fertilizer == "B", ] 
print("fert B mean height: ")
mean(fert_B_df[["Height_cm"]])
print("fert B mean tomatoes: ")
mean(fert_B_df[["Number_of_Tomatoes"]])

fert_C_df = df[df$Fertilizer == "C", ] 
print("fert C mean height: ")
mean(fert_C_df[["Height_cm"]])
print("fert C mean tomatoes: ")
mean(fert_C_df[["Number_of_Tomatoes"]])

#create the plot for height vs num tomatoes
plot(fert_A_df$Height_cm, fert_A_df$Number_of_Tomatoes,
     main = "Height vs Number of Tomatoes by Fertilizer",
     xlab = "Height (cm)", ylab = "Number of Tomatoes",
     pch = 19, col = "red", xlim = range(df$Height_cm),
     ylim = range(df$Number_of_Tomatoes))

#add fertilizers b and c to the plot with different colors
points(fert_B_df$Height_cm, fert_B_df$Number_of_Tomatoes, pch = 19, col = "green")
points(fert_C_df$Height_cm, fert_C_df$Number_of_Tomatoes, pch = 19, col = "blue")

#add a legend to the plot with the appropriate color fertilizer mapping
legend("topright",
       legend = c("Fertilizer A", "Fertilizer B", "Fertilizer C"),
       col = c("red", "green", "blue"),
       pch = 19)
