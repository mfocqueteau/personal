
// typedefs
typedef struct terminal Terminal;
typedef struct door Door;
typedef struct queue Queue;
typedef struct passenger Passenger;

struct terminal
{
  Door **compuertas;
};

struct door
{
  char id;
  Queue *cola;
};

struct queue
{
  Passenger *primero;
  unsigned length;
};

struct passenger
{
  int ID_pasajero;
  char *tipo;
};
