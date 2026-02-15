package com.learnJava;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.function.Function;
import java.util.function.UnaryOperator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;


public class ACheck {

    public static Optional<Integer> op(Integer oo){
if(oo>9)
        return Optional.ofNullable(oo);
else return Optional.empty();
    }
    public static void main(String[] args) {

       System.out.println( op(9));
        System.out.println( "hhhhhhhhhhhhhh");
//        List<Integer> al = Arrays.asList(1,2,3,4,5);
//        IntStream intStream = al.stream().mapToInt(Integer::intValue);
//        IntStream i= IntStream.of(1,2,3,4);
//System.out.println(i.max().isPresent());
//       Stream.generate(() -> "rr").limit(2).forEach(s->System.out.println(s));
//        Comparator<Integer> c = ACheck::compare;
//        System.out.println(c.compare(1,2));

//        LocalDate localDate = LocalDate.now();
//        System.out.println("Current Date is " + localDate);
//UnaryOperator
//        Function
    }










    private static int compare(Integer a, Integer b) {
        if (a > b) return 1;
        if (a < b) return -1;
        return 0;
    }
}