class Solution {
    public int solution(int n) {
        
        int result = 0; 
        
        for (int i = 1; i <= n; i++) {
            if (count(i) >= 3) {
                result++; 
            }
        }
        
        return result; 
    }
    
    private int count(int num) {
        int count = 0; 
        for (int i = 1; i <= num; i++) {
            if (num % i == 0) {
                count++; 
            }
        }
        return count; 
    }
}