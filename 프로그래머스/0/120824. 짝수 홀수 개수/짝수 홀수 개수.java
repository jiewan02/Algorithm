class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        answer = new int[2];
        int oddIdx = 0; 
        int evenIdx = 0; 
        for (int i = 0; i < num_list.length; i++) {
            if (num_list[i] % 2 == 0) {
                evenIdx++;
            } else {
                oddIdx++; 
            }
        }
        answer[0] = evenIdx;
        answer[1] = oddIdx; 
        return answer;
    }
}