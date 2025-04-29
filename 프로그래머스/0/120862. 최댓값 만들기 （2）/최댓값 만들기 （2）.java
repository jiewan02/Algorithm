import java.util.*; 

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers); 
        
        answer = numbers.length; 
        int max1 = numbers[answer-1] * numbers[answer-2]; 
        int max2 = numbers[0] * numbers[1]; 
        answer = Math.max(max1, max2); 
        
        return answer;
    }
}