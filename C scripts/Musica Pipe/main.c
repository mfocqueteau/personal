#include <stdio.h>
#include <stdlib.h>

typedef struct song {
  int length;
  int rating;
} Song;

Song* song_init(int length, int rating) {
  Song* new_song = malloc(sizeof(Song));
  *new_song = (Song) { .length = length, .rating = rating };
  return new_song;
}


int main() {
  Song* my_song = song_init(3, 4);
  printf("Datos de my_song:\nDuración: %d\nRating: %d\n", my_song->length, my_song->rating);
  free(my_song);
  return 0;
}
