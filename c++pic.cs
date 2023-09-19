using System;
using System.IO;
using System.Collections.Generic;

class Program
{
    static int ngCounter = 0;
    static Queue<string> ngImages = new Queue<string>();
    const int MaxNGImages = 10;

    static void Main(string[] args)
    {
        string imagePath = "path_to_your_image_folder";

        while (true)
        {
            // Simulate image collection and classification
            string imageName = CollectImage(imagePath);
            bool isNice = ClassifyImage(imageName);

            // Update counters and folders
            if (isNice)
            {
                MoveToNiceFolder(imageName);
            }
            else
            {
                ngCounter++;
                ngImages.Enqueue(imageName);
                if (ngImages.Count > MaxNGImages)
                {
                    ngImages.Dequeue();
                }
                if (ngCounter >= 10)
                {
                    DisplayNGImage();
                    ngCounter = 0;
                }
            }
        }
    }

    static string CollectImage(string path)
    {
        // Simulate image collection logic
        // Return image file name
        return "image.jpg";
    }

    static bool ClassifyImage(string imageName)
    {
        // Simulate image classification logic
        // Return true if image is classified as NICE, false if NG
        return true;
    }

    static void MoveToNiceFolder(string imageName)
    {
        // Simulate moving image to NICE folder
        string sourcePath = "path_to_your_image_folder";
        string destinationPath = "path_to_nice_folder";
        File.Move(Path.Combine(sourcePath, imageName), Path.Combine(destinationPath, imageName));
    }

    static void DisplayNGImage()
    {
        // Display the first NG image
        string ngImageName = ngImages.Dequeue();
        string ngFolderPath = "path_to_ng_folder";
        string ngImagePath = Path.Combine(ngFolderPath, ngImageName);

        // Simulate displaying the image
        Console.WriteLine($"Displaying NG image: {ngImagePath}");
    }
}
