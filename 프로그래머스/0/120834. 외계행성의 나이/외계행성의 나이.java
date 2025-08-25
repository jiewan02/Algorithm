class Solution {
    public String solution(int age) {
        
        String s = String.valueOf(age); 
        StringBuilder sb = new StringBuilder(); 
        
        for (int i = 0; i < s.length(); i++) {
            int digit = s.charAt(i) - '0'; 
            char c = (char) ('a' + digit); 
            sb.append(c); 
        }
        
        return sb.toString(); 
    }
}