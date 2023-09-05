#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare ( const void *pa, const void *pb ) {
    const int *a = *(const int **)pa;
    const int *b = *(const int **)pb;

    if(a[1] == b[1])
        return a[0] - b[0];
    else
        return a[1] - b[1];
}

// targets_rows는 2차원 배열 targets의 행 길이, targets_cols는 2차원 배열 targets의 열 길이입니다.
int solution(int** targets, size_t targets_rows, size_t targets_cols) {
    int answer = 0;
    int count = 0;

    qsort(targets,targets_rows,2*sizeof(int),compare);

    while(count<targets_rows){
        int last_distance = targets[count][1];
        for(int j=count+1;j<targets_rows;j++){
            if (targets[j][0] >=last_distance){
                break;
            }
            else{count+=1;}
        }
        answer +=1;
        count+=1;
    }

    return answer;
}
