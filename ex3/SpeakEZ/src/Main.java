import opennlp.tools.postag.POSModel;
import opennlp.tools.postag.POSTaggerME;
import opennlp.tools.sentdetect.*;
import opennlp.tools.sentdetect.SentenceModel;
import opennlp.tools.util.InvalidFormatException;
import  opennlp.tools.stemmer.PorterStemmer;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.regex.Pattern;
import java.util.stream.Stream;

import static java.util.function.Function.identity;
import static java.util.stream.Collectors.*;

public class Main {

    public static void main(String[] args) {

        System.out.println("Fuck off!");

        System.out.println("Working Directory = " +
                System.getProperty("user.dir"));
        InputStream modelIn = null;
        try {
            modelIn = new FileInputStream("en-pos-maxent.bin");
            POSModel model = new POSModel(modelIn);
            POSTaggerME tagger = new POSTaggerME(model);
            String content = new Scanner(new File("NovaPlasma.txt")).useDelimiter("\\Z").next();
            String[] splited = content.split("\\s+");
            int j = 0 ;
            for (String word : splited) {
                splited[j] = word.replaceAll("[^\\p{L}\\p{Nd}]+", "");
                j++ ;
            }
            String[] lowerCase =new String[splited.length];
            for (int i=0; i<lowerCase.length; ++i)
            {
                lowerCase[i] = splited[i].toLowerCase();
            }

            System.out.print(Arrays.toString(splited)+"\n");
            System.out.print(Arrays.toString(lowerCase)+"\n");


            String tags[] = tagger.tag(splited);
            String tags2[] = tagger.tag(lowerCase);
            System.out.print(Arrays.toString(tags)+"\n");
            System.out.print(Arrays.toString(tags2)+"\n");
            PorterStemmer ps = new PorterStemmer();
            String[] stemArray= new String[splited.length];
            int i = 0;
            for (String word : lowerCase) {
                String stem = ps.stem(word);
                stemArray[i] = stem ;
                i++;
                System.out.println("Word: " + word + "  Stem: " + stem);
            }
            String[] words = splited;
            Set<String> uniqueWords = new HashSet<String>();

            for (String word : words) {
                uniqueWords.add(word);
            }
            System.out.println("size before stemming: "+uniqueWords.size());
             words = stemArray;
            uniqueWords = new HashSet<String>();

            for (String word : words) {
                uniqueWords.add(word);
            }
            System.out.println("size after stemming: "+uniqueWords.size());

        }
        catch (IOException e) {
            // Model loading failed, handle the error
            e.printStackTrace();
        }
        finally {
            if (modelIn != null) {
                try {
                    modelIn.close();
                }
                catch (IOException e) {
                }
            }
        }


    }



}
