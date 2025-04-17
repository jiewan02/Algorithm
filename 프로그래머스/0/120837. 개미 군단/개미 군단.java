class Solution {
    public int solution(int hp) {
        int answer = 0; 
        int gen = hp / 5; 
        int remain = hp % 5; 
        
        int mid = remain / 3; 
        remain = remain % 3; 
        
        int low = remain; 
        
        answer = gen + mid + low; 
        
        return answer;
    }
}