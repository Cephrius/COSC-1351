package twitchURL;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;

public class TwitchURL {
    private String[] adj1;
    private String[] adj2;
    private String[] nouns;
    private String[] emotes;

    public TwitchURL() throws FileNotFoundException {
        adj1 = readWordsFromFile("C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\twitchURL\\adjective1.txt");
        adj2 = readWordsFromFile("C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\twitchURL\\adjective2.txt");
        nouns = readWordsFromFile("C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\twitchURL\\nouns.txt");
        emotes = readWordsFromFile("C:\\Users\\theac\\OneDrive\\Documents\\COSC-1351\\twitchURL\\emotes.txt");
    }

    private String[] readWordsFromFile(String fileName) throws FileNotFoundException {
        String[] words = new String[10]; // Assuming each file has 10 entries
        int index = 0;

        Scanner scanner = new Scanner(new File(fileName));
        while (scanner.hasNext() && index < 10) {
            words[index] = scanner.next();
            index++;
        }
        scanner.close();

        return words;
    }

    public String generateTwitchClipURL() {
        Random random = new Random();
        String adjective1 = adj1[random.nextInt(adj1.length)];
        String adjective2 = adj2[random.nextInt(adj2.length)];
        String noun = nouns[random.nextInt(nouns.length)];
        String emote = emotes[random.nextInt(emotes.length)];

        return "https://www.twitch.tv/" + adjective1 + adjective2 + noun + emote;
    }

    public static void main(String[] args) {
        try {
            TwitchURL generator = new TwitchURL();
            String clipURL = generator.generateTwitchClipURL();
            System.out.println("Generated Twitch Clip URL: " + clipURL);
        } catch (FileNotFoundException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
