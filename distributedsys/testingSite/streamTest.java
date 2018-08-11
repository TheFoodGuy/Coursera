import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.stream.Stream;
import java.util.stream.Collectors;
import java.util.Arrays;
/*
    Testing out how java stream works in some weird cases
    I'm just testing out some functions so I could finish mini_project_2
    for parallel programming in java course

    Implementing mostCommonFistNameOfInactiveStudentsParallelStream
    This tries to find the most common last name of inactive students only
*/
public class streamTest {
    public static void main(String[] args){
        System.out.println("Hello, World"); 
        // Let's do four students as a test 
        Student one = new Student("David", "Liang", 22, 90, false);
        Student two = new Student("Bob", "Liang", 50, 95, false);
        Student three = new Student("Emily", "Billy", 20, 85, true); 
        Student four = new Student("Ryan", "Bob", 21, 100, false); 
        
        List<Student> inactiveStudents = new ArrayList<Student>();
        inactiveStudents.add(one);
        inactiveStudents.add(two);
        inactiveStudents.add(three);
        inactiveStudents.add(four);         
        
        // now using java stream to filter out this issue 
        

        // other testing down here 
        // Map<String, Double> lastNamePoints = Stream.of(inactiveStudents)
        //     .parallel()


        // lastNamePoints
        //     .forEach((key, value) -> System.out.format("first Name : %s at %s\n", key, value));
    
        Stream<String> stream = 
            Stream.of("a", "b", "c").filter(element -> element.contains("b"));

        List<String> myList = Arrays.asList("a1", "a2", "b1", "c2", "c1");
        myList
            .stream()
            .filter(s -> s.startsWith("c"))
            .map(String::toUpperCase)
            .sorted()
            .forEach(System.out::println);
        
        Map<String, Double> inactive = 
            inactiveStudents
                .stream()
                .filter(s -> !s.checkIsCurrent())
                .collect(Collectors.toMap(Student::getFirstName, Collectors.counting()))
    }
}

