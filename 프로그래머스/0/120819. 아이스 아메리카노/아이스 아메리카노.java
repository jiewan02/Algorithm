class Solution {
    public int[] solution(int money) {
        int[] answer = {};
        answer = new int[2]; 
        int coffee = money / 5500; 
        answer[0] = coffee; 
        answer[1] = money - coffee * 5500; 
        return answer;
    }
}