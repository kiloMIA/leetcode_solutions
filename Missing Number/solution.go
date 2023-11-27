package main

func missingNumber(nums []int) int {
    n := len(nums)
    total_sum := int((n*(n+1)/2))
    sum := 0
    for _, v := range nums {
        sum += v
    }
    return total_sum - sum
}