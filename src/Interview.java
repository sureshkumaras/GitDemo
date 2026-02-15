import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Interview {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = {1,1,2,2,2,4,4,4,4,4};
		
		Map<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();
		for(int t : a) {
			map.put(t, map.getOrDefault(t, 0)+1);
		}
//		System.out.println(map);
		
		for(Entry<Integer, Integer> m : map.entrySet()) {
//			System.out.println(m.get);
		}
		
		int aa=10;
		Integer ww = aa;
		aa=ww;
	}

}
