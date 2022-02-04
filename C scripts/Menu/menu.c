#include <stdio.h>
#include <stdlib.h>

typedef struct menu {
  char** options;
  char length;
} Menu;

Menu* menu_init(char** options, char length) {
  Menu* myMenu = malloc(sizeof(Menu));
  myMenu->length = length;
  myMenu->options = calloc(length, sizeof(char*));
  for (char i = 0; i < length; i++) {
    myMenu->options[i] = options[i];
  }
  return myMenu;
}

void display_menu(Menu* menu) {
  for (char i = 0; i < menu->length; i++) {
    printf("[%hhd] %s\n", i + 1, menu->options[i]);
  }
  unsigned char chosen;
  printf("Ingrese una opción: ");
  scanf("%hhd", &chosen);
  while (chosen <= 0 || menu->length < chosen) {
    printf("ERROR: debes ingresar el índice de la opción\n\n");
    printf("Ingrese una opción: ");
    scanf("%hhu", &chosen);
  }
  chosen--;
  printf("Haz seleccionado: %s\n", menu->options[chosen]);
}

void destroy_menu(Menu* menu) {
  free(menu->options);
  free(menu);
}

int main() {
  char* myOptions[5] = {"Automóvil", "Motocicleta", "Transporte público",
                        "Bicicleta", "Caminata"};
  Menu* myMenu = menu_init(myOptions, 5);
  display_menu(myMenu);
  destroy_menu(myMenu);
  return 0;
}
