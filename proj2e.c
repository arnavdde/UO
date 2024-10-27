#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *read_file(const char *filename, long *file_size) {
    FILE *file = fopen(filename, "rb");
    if (!file) {
        printf("\"%s\" is not a valid file\n", filename);
        exit(1);
    }

    fseek(file, 0, SEEK_END);
    *file_size = ftell(file);
    if (*file_size == -1) {
        fclose(file);
        printf("Error seeking file size\n");
        exit(1);
    }

    fseek(file, 0, SEEK_SET);
    char *content = (char *)malloc(*file_size + 1);
    if (!content) {
        fclose(file);
        printf("Error in malloc\n");
        exit(1);
    }

    size_t read_size = fread(content, 1, *file_size, file);
    if (read_size != *file_size) {
        free(content);
        fclose(file);
        printf("Error reading file\n");
        exit(1);
    }

    content[*file_size] = '\0';
    fclose(file);
    return content;
}

int is_delimiter(char c) {
    return c == ' ' || c == ',' || c == '.' || c == '\n' || c == '\t';
}

int count_word_occurrences(char *content, const char *word, int word_len) {
    int count = 0;
    char *ptr = content;

    while (*ptr != '\0') {
        while (is_delimiter(*ptr) && *ptr != '\0') ptr++;

        if (strncmp(ptr, word, word_len) == 0 &&
            (is_delimiter(ptr[word_len]) || ptr[word_len] == '\0')) {
            count++;
        }

        while (!is_delimiter(*ptr) && *ptr != '\0') ptr++;
    }
    return count;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("IN: %s filename word1 [word2 ... wordN]\n", argv[0]);
        return 1;
    }

    char *filename = argv[1];
    long file_size;
    char *file_content = read_file(filename, &file_size);
    if (!file_content) {
        return 1;
    }

    int *counters = (int *)malloc((argc - 2) * sizeof(int));
    if (!counters) {
        free(file_content);
        printf("Memory allocation error\n");
        return 1;
    }

    for (int i = 0; i < argc - 2; i++) {
        counters[i] = 0;
    }

    for (int i = 2; i < argc; i++) {
        int word_len = strlen(argv[i]);
        counters[i - 2] = count_word_occurrences(file_content, argv[i], word_len);
    }

    for (int i = 2; i < argc; i++) {
        printf("The word \"%s\" occurs %d times.\n", argv[i], counters[i - 2]);
    }

    free(file_content);
    free(counters);

    return 0;
}
