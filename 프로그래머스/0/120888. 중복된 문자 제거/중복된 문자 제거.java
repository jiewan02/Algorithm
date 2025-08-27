import java.util.*; 

class Solution {
    public String solution(String my_string) {
        char[] c = my_string.toCharArray(); 
        StringBuilder sb = new StringBuilder(); 
        
        LinkedHashSet<Character> lhs = new LinkedHashSet<Character>(); 
        for (char ch : c) {
            lhs.add(ch); 
        }
        
        for (Character character : lhs) {
            sb.append(character); 
        }
        
        return sb.toString(); 
        
    }
}