public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var dict = new Dictionary<int,int> ();
        for (int i = 0 ; i < nums.Length; i ++) {
             if(dict.ContainsKey(nums[i])) {
                dict[nums[i]]++;
             }
             else {
             dict[nums[i]] = 1;
             }
        }
        var heap = new PriorityQueue<int,int>();
        foreach(var entry in dict) {
            heap.Enqueue(entry.Key,entry.Value);
            if (heap.Count > k){
                 heap.Dequeue();
            }
        }
        var res = new int[k];
        for (int i =0; i <k; i++) {
            res[i] = heap.Dequeue();
        }
        return res;
    }
}
