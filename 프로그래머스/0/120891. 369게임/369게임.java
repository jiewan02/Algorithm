class Solution {
    public int solution(int order) {
        String mystring = String.valueOf(order);
        int count = 0; 
        
        for (int i = 0; i < mystring.length(); i++) {
            char c = mystring.charAt(i); 
            if (c == '3' || c== '6' || c == '9') {
                count++; 
            }
        }
        
        return count; 
        
    }
}