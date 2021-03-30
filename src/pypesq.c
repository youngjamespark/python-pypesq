#include <stdio.h>
#include <math.h>
// #include "pesq/pesq.h"
// #include "pesq/dsp.h"
#include "..\pesq\pesqmain.h"

#define ITU_RESULTS_FILE          "pesq_results.txt"

double evaluate(char* reference, char* degraded, int sample_rate, char* mode) {
    double mos;
    // printf("reference = %s\n", reference);
    // printf("degraded = %s\n", degraded);
    // printf("sample rate = %d\n", sample_rate);
    // printf("mode = %s\n", mode);

    mos = pesq_main(reference, degraded, sample_rate, mode);
        
    return mos;
}
