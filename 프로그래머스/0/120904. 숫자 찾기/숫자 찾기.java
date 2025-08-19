class Solution {
    public int solution(int num, int k) {
        int idx = -1; 
        String s = String.valueOf(num); 
        
        idx = s.indexOf(String.valueOf(k)); 
        
        if (idx != -1) {
            return idx + 1; 
        } else {
            return idx; 
        }
        
    }
}