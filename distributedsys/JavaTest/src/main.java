import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class main{
    public interface Task{
        void run();
        default void cancel(){

        }
    }

    public static void schedule(Task task){
        task.run();
    }

    public static void main(String[] args){
        schedule(() -> System.out.println("Hello World"));
        List<String> versions = Arrays.asList("java 7", "java 8");
        Comparator<? super String> comparator = String::compareTo;
        versions.sort(comparator);

        System.out.println("Language versions:" + versions);
        versions.parallelStream().filter(s -> s.equals("java 8")).map(s -> "Develop in " + s + " with Pleasure!").forEach(System.out::println);

        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd","", "jkl");
        List<String> filtered = strings.stream().filter(string -> !string.isEmpty()).collect(Collectors.toList());

    }
}