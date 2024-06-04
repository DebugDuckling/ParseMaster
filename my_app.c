#include <gtk/gtk.h>

// Callback function to handle window close event
static void on_destroy(GtkWidget *widget, gpointer data) {
    gtk_main_quit();
}

// Load CSS file
void load_css(void) {
    GtkCssProvider *provider;
    GdkDisplay *display;
    GdkScreen *screen;

    provider = gtk_css_provider_new();
    display = gdk_display_get_default();
    screen = gdk_display_get_default_screen(display);
    gtk_style_context_add_provider_for_screen(screen, GTK_STYLE_PROVIDER(provider), GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);

    const gchar *css_path = "style.css";
    GError *error = NULL;
    gtk_css_provider_load_from_path(provider, css_path, &error);

    if (error != NULL) {
        g_printerr("Error loading CSS file: %s\n", error->message);
        g_clear_error(&error);
    }

    g_object_unref(provider);
}

// Function to set adjustments for spin buttons and scales
void set_adjustments(GtkBuilder *builder) {
    GObject *obj;
    GSList *objects = gtk_builder_get_objects(builder);
    GSList *iter;

    for (iter = objects; iter != NULL; iter = g_slist_next(iter)) {
        obj = G_OBJECT(iter->data);
        if (GTK_IS_SPIN_BUTTON(obj)) {
            GtkAdjustment *adjustment = gtk_adjustment_new(0, 0, 100, 1, 10, 0);
            gtk_spin_button_set_adjustment(GTK_SPIN_BUTTON(obj), adjustment);
        } else if (GTK_IS_SCALE(obj)) {
            GtkAdjustment *adjustment = gtk_adjustment_new(0, 0, 100, 1, 10, 0);
            gtk_range_set_adjustment(GTK_RANGE(obj), adjustment);
        }
    }
    g_slist_free(objects);
}

int main(int argc, char *argv[]) {
    GtkBuilder *builder;
    GtkWidget *window;
    GError *error = NULL;

    // Initialize GTK
    gtk_init(&argc, &argv);

    // Load CSS
    load_css();

    // Create a new GtkBuilder instance
    builder = gtk_builder_new();

    // Load the UI description from the glade file
    if (gtk_builder_add_from_file(builder, "gui.glade", &error) == 0) {
        g_printerr("Error loading file: %s\n", error->message);
        g_clear_error(&error);
        return 1;
    }

    // Get the main window object from the UI description
    window = GTK_WIDGET(gtk_builder_get_object(builder, "main_window"));

    if (!window) {
        g_printerr("Unable to find object with ID 'main_window'\n");
        return 1;
    }

    // Set adjustments for spin buttons and scales
    set_adjustments(builder);

    // Connect the window's destroy signal to the callback function
    g_signal_connect(window, "destroy", G_CALLBACK(on_destroy), NULL);

    // Show the window and all its child widgets
    gtk_widget_show_all(window);

    // Enter the GTK main loop
    gtk_main();

    // Clean up
    g_object_unref(builder);

    return 0;
}
