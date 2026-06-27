public class Solution {
    public bool IsValid(string s) {
        Stack<char> charStack = new();
		Dictionary <char,char>  closeToOpen =new Dictionary<char,char> {
			{')','('},
			{']','['},
			{'}', '{'}
			
		};
		foreach(char c in s) {
			if(closeToOpen.TryGetValue(c,out char value)){
				if(charStack.Count()> 0 && charStack.Peek() == value) {
					charStack.Pop();
				}
				else {
				return false;
				}
			} else  {
				charStack.Push(c);
			}
		}
		return charStack.Count() == 0;
    }
}
