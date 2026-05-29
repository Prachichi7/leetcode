class Solution {
    public int minElement(int[] nums) {
        int minDigitSum = 100;
      
        for (int number : nums) {
            int digitSum = 0;
          
            while (number > 0) {
                digitSum += number % 10;  // Add the last digit to the sum
                number /= 10;              // Remove the last digit
            }
          
            minDigitSum = Math.min(minDigitSum, digitSum);
        }
      
        return minDigitSum;
    }
}