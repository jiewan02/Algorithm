class Solution {
    public int solution(int n) {
        int amount =  1; 
        
        while ((amount * 6) % n != 0) {
            amount++; 
        }
        
        return amount; 
    }
}