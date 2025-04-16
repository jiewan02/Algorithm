class Solution {
    public int[] solution(int n) {
        int[] answer = {};
        int count = 0; 
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                count++; 
            }
        }
        answer = new int[count]; 
        int idx = 0; 
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) {
                answer[idx] = i; 
                idx++; 
            }
        }
        return answer;
    }
}