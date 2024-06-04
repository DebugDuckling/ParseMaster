# Makefile

# Compiler
CC = gcc

# Compiler flags
CFLAGS = `pkg-config --cflags gtk+-3.0`

# Linker flags
LDFLAGS = `pkg-config --libs gtk+-3.0`

# Source files
SRCS = my_app.c

# Output binary
TARGET = my_app

# Default target
all: $(TARGET)

# Compile the program
$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRCS) $(LDFLAGS)

# Clean up build artifacts
clean:
	rm -f $(TARGET)

.PHONY: all clean
