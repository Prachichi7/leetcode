class Solution {
    public int myAtoi(String s) {
        if (s == null) return 0;
      
        int length = s.length();
        if (length == 0) return 0;
      
        int index = 0;
        while (index < length && s.charAt(index) == ' ') {
            index++;
        }
      
        if (index == length) return 0;
      
        int sign = 1;
        if (s.charAt(index) == '-') {
            sign = -1;
        }
      
        if (s.charAt(index) == '-' || s.charAt(index) == '+') {
            index++;
        }
      
        int result = 0;
        int overflowThreshold = Integer.MAX_VALUE / 10;
      
        while (index < length) {
            char currentChar = s.charAt(index);
          
            if (currentChar < '0' || currentChar > '9') {
                break;
            }
          
            if (result > overflowThreshold || 
                (result == overflowThreshold && currentChar > '7')) {
                return sign > 0 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
          
            result = result * 10 + (currentChar - '0');
            index++;
        }
      
        return sign * result;
    }
}