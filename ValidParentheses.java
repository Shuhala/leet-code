package leet;

import com.sun.xml.internal.ws.util.StringUtils;

import java.text.StringCharacterIterator;
import java.util.*;
import java.util.function.BiPredicate;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 */
public class ValidParentheses {

    public static void main(String[] args) {
        System.out.println(isValid("((([]])))"));
    }

    private static boolean isValid(String s) {

        Map<Character, Integer> occurences = s.chars().boxed()
                .collect(Collectors.toMap(
                        k -> ((char) k.intValue()),
                        v -> 1,
                        Integer::sum
                ));

        BiPredicate<Character, Character> isBalanced = (a, b) ->
                Objects.equals(occurences.get(a), occurences.get(b));

        if( !isBalanced.test('(',')')
                || !isBalanced.test('[',']')
                || !isBalanced.test('{','}'))
            return false;


        HashMap<Character, Character> brackets = new HashMap<Character, Character>(){
            {
                put(')','(');
                put(']','[');
                put('}','{');
            }
        };

        Stack<Character> stack = new Stack<>();
        Predicate<Character> isAnOpenParenthesis = brackets::containsValue;
        Predicate<Character> isClosingAParenthesis = (c) -> brackets.get(c) == stack.pop();

        for (Character c: s.toCharArray()){
            if(isAnOpenParenthesis.test(c)) stack.push(c);
            else if(stack.empty() || !isClosingAParenthesis.test(c)) return false;
        }

        return stack.empty();
    }
}

//        long nbParenthesis = s.chars().filter(c -> (int) '(' == c || (int) ')' == c).count();
//        long nbBrackets = s.chars().filter(c -> (int) '[' == c || (int) ']' == c).count();
//        long nbBraces = s.chars().filter(c -> (int) '{' == c || (int) '}' == c).count();
//        Predicate<Long> isNotBalanced = (l) -> l % 2 != 0;
//
//        if(isNotBalanced.test(nbParenthesis) || isNotBalanced.test(nbBrackets) || isNotBalanced.test(nbBraces))
//            return false;


//    Map<Character, Integer> groupedValues = s.chars().boxed()
//            .collect(Collectors.toMap(
//                    k -> ((char) k.intValue()),
//                    v -> 1,
//                    Integer::sum
//            ));
