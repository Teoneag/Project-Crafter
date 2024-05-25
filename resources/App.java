package com.teoneag;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

public class App extends JFrame {
    private final JPanel mainContent = new JPanel(new BorderLayout());

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new App().setVisible(true));
    }

    public App() {
        setTitle("Table Editor");
        setSize(800, 600);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        add(mainContent, BorderLayout.CENTER);

        createMenuBar();
        createNoTableMessage();
    }

    private void newFile() {
        // ToDo
    }

    private void openFile() {
        // ToDo
    }

    private void saveFile() {
        // ToDo
    }

    private void saveAsFile() {
        // ToDo
    }

    private void exit() {
        // ToDo
    }

    private void undo() {
        // ToDo
    }

    private void redo() {
        // ToDo
    }

    private void cut() {
        // ToDo
    }

    private void copy() {
        // ToDo
    }

    private void paste() {
        // ToDo
    }

    private void insertRow() {
        // ToDo
    }

    private void insertColumn() {
        // ToDo
    }

    private void deleteRow() {
        // ToDo
    }

    private void deleteColumn() {
        // ToDo
    }

    private void about() {
        // ToDo
    }

    private void createMenuBar() {
        JMenuBar menuBar = new JMenuBar();

        JMenu fileMenu = new JMenu("File");
        addMenuItem(fileMenu, "New", e -> newFile());
        addMenuItem(fileMenu, "Open", e -> openFile());
        addMenuItem(fileMenu, "Save", e -> saveFile());
        addMenuItem(fileMenu, "Save As", e -> saveAsFile());
        addMenuItem(fileMenu, "Exit", e -> exit());
        menuBar.add(fileMenu);

        JMenu editMenu = new JMenu("Edit");
        addMenuItem(editMenu, "Undo", e -> undo());
        addMenuItem(editMenu, "Redo", e -> redo());
        addMenuItem(editMenu, "Cut", e -> cut());
        addMenuItem(editMenu, "Copy", e -> copy());
        addMenuItem(editMenu, "Paste", e -> paste());
        menuBar.add(editMenu);

        JMenu tableMenu = new JMenu("Table");
        addMenuItem(tableMenu, "Insert Row", e -> insertRow());
        addMenuItem(tableMenu, "Insert Column", e -> insertColumn());
        addMenuItem(tableMenu, "Delete Row", e -> deleteRow());
        addMenuItem(tableMenu, "Delete Column", e -> deleteColumn());
        menuBar.add(tableMenu);

        JMenu helpMenu = new JMenu("Help");
        addMenuItem(helpMenu, "About", e -> about());
        menuBar.add(helpMenu);

        setJMenuBar(menuBar);
    }

    private void createNoTableMessage() {
        JLabel label = new JLabel("No table opened, create a ");
        JButton newButton = new JButton("new");
        newButton.addActionListener(e -> newFile());
        JLabel label2 = new JLabel(" table or ");
        JButton openButton = new JButton("open");
        openButton.addActionListener(e -> openFile());
        JLabel label3 = new JLabel(" one.");

        JPanel messagePanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        messagePanel.add(label);
        messagePanel.add(newButton);
        messagePanel.add(label2);
        messagePanel.add(openButton);
        messagePanel.add(label3);

        displayOnCenter(messagePanel);
    }

    private void displayOnCenter(Component component) {
        mainContent.removeAll();
        JPanel centerPanel = new JPanel(new GridBagLayout());
        centerPanel.add(component);
        mainContent.add(centerPanel, BorderLayout.CENTER);
        revalidate();
        repaint();
    }

    private void displayOnFull(Component component) {
        mainContent.removeAll();
        mainContent.add(component, BorderLayout.CENTER);
        revalidate();
        repaint();
    }

    private void addMenuItem(JMenu menu, String name, ActionListener listener) {
        JMenuItem menuItem = new JMenuItem(name);
        menuItem.addActionListener(listener);
        menu.add(menuItem);
    }
}
