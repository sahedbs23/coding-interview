// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class IsPrimeNumber {
    public static void main(String[] args) {
        System.out.println(isPrime(17));
    }
    
    static boolean isPrime(int n){
        for(int i =2; i*i <= n; i++){
            if(n%i == 0){
                return false;
            }
        }
        
        return true;
    }
}
