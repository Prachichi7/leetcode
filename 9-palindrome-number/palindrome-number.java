class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x > 0 && x % 10 == 0)) {
            return false;
        }
      
        int reversehalf = 0;
      
        while (reversehalf < x) {
            reversehalf = reversehalf * 10 + x % 10;
            x /= 10;
        }
      
        return x == reversehalf || x == reversehalf / 10;
    }
}