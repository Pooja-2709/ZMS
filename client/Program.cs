using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

var app = builder.Build();

app.MapControllers();

app.Run();



/*using System.Threading.Tasks;
using Grpc.Net.Client;
using GrpcClient;

internal class Program
{
    private static async Task Main(string[] args)
    {
        // The port number must match the port of the gRPC server.
        using var channel = GrpcChannel.ForAddress("http://localhost:50051");
        var client = new Student.StudentClient(channel);
        // var reply = await client.SayHelloAsync(
        //                   new HelloRequest { Name = "GreeterClient" });
        // Console.WriteLine("Greeting: " + reply.Message);
        var request = new CreateRequest() {
            Name = "Abhishek",
            Lastname = "Chavan"
        };
        var reply = await client.createAsync(request);
        Console.WriteLine("Student:" + reply);

        // var request1 = new DeleteRequest(){
        //     Id = 1
        // };

        // var reply_delete = await client.deleteAsync(request1);
        // Console.WriteLine("Item Deleted");
    }
}
*/
















