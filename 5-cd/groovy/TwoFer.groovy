class TwoFer {

    static String twoFer(String name) {
        // if (!name) {
        //     "One for you, one for me."
        // } else {
        //     "One for $name, one for me."
        // }
        // "One for ${name == null ? 'you' : name}, one for me."
        "One for ${name ?: 'you'}, one for me."
    }
}
