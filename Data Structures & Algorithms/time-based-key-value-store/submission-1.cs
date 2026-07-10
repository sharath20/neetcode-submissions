public class TimeMap {
    private Dictionary<string,SortedList<int,string>> keyValue;

    public TimeMap() {
        keyValue = new Dictionary<string,SortedList<int,string>>();
    }
    
    public void Set(string key, string value, int timestamp) {

        if(!keyValue.ContainsKey(key)) {
            keyValue[key] = new SortedList<int,string> ();
        }
        keyValue[key][timestamp] = value;
        
    }
    
    public string Get(string key, int timestamp) {
        if(!keyValue.ContainsKey(key)) return "";
        var timeStamps = keyValue[key]; 
        int left = 0;
        int right = timeStamps.Count -1;
        
        while (left <= right) {
            int mid = left + (right-left)/2;
            if(timeStamps.Keys[mid] == timestamp)
            {
                return timeStamps.Values[mid];
            }

            if(timeStamps.Keys[mid] <= timestamp ) {

                left = mid + 1;
            } else {
                right = mid -1;
            }

        }
        if(right >= 0) 
            {
                return timeStamps.Values[right];
            }
            return "";
    }
}
