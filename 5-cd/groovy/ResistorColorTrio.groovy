class ResistorColorTrio {

    static final colors = ['black', 'brown', 'red', 'orange', 'yellow',
                           'green', 'blue', 'violet', 'grey', 'white']

    static String label(List<String> input) {
        def nums = input.collect { colors.indexOf(it) }
        def zeros = nums[2]
        def ohms = "${nums.take(2).join()}${'0'.repeat(zeros)}" as int
        ohms > 1000 ? "${ohms / 1000} kiloohms" : "$ohms ohms"
    }

}
