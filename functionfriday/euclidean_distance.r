euclidean_distance <- function(vector_1, vector_2) {
    if (length(vector_1) != length(vector_2)) {
        stop("Vectors must have the same length.")
    }
    sum_of_squared_differences <- sum((vector_1 - vector_2)^2)
    result <- sqrt(sum_of_squared_differences)
    return(result)
}
