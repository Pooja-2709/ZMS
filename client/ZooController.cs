using Google.Protobuf;
using Grpc.Core;
using Grpc.Net.Client;
using GrpcClient;
using Microsoft.AspNetCore.Mvc;
using System.Text;
using System.Text.Json;
namespace Controller.Zoo;

[Route("api/zoocontroller")]

public class ZooController : ControllerBase
{
    private readonly GrpcChannel channel;

    private readonly ZooService.ZooServiceClient client;

    public ZooController()
    {
        channel = GrpcChannel.ForAddress("http://localhost:50051");
        client = new ZooService.ZooServiceClient(channel);
    }

    [HttpPost("create")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]

    public async Task<ActionResult> Create()
    {
        var request = await CreateProtobufMessage<CreateZooRequest>(Request.Body);
        var response = await client.createAsync(request);
        return Ok(response);

    }
    
    [HttpPut("update")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> update()
    {
        var request = await CreateProtobufMessage<UpdateZooRequest>(Request.Body);
        var response = await client.updateAsync(request);
        return Ok(response);

    }

    [HttpDelete("delete")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> delete()
    {
        var request = await CreateProtobufMessage<DeleteZooRequest>(Request.Body);
        var response = await client.deleteAsync(request);
        return Ok(response);
    }

    
    [HttpGet("search")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> search()
    {
        var request = await CreateProtobufMessage<ReadAllZooRequest>(Request.Body);
        var response = await client.searchAsync(request);
        return Ok(response);
    }

    [HttpGet("get")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> get()
    {
        var request = await CreateProtobufMessage<GetZooRequest>(Request.Body);
        var response = await client.getAsync(request);
        return Ok(response);
    }


    /// <summary>
    /// Create Protobuf Message from the json request
    /// </summary>
    /// <param name="body">Request in sequence of bytes</param>
    /// <typeparam name="U">Message Type</typeparam>
    /// <returns>Protobuf Message</returns>
    private async Task<U> CreateProtobufMessage<U>(Stream body) where U : IMessage<U>, new()
    {
        using (StreamReader reader = new StreamReader(body, Encoding.UTF8))
        {
            var json = await reader.ReadToEndAsync();

            json = json.Replace("\r\n", string.Empty).Replace("\r", string.Empty).Replace("\n", string.Empty);

            if (string.IsNullOrWhiteSpace(json))
            {
                throw new RpcException(new Status(Grpc.Core.StatusCode.Internal, "Request Body Empty. (Using StudentsController)"));
            }

            try
            {
                if (IsJsonObjectEmpty(json))
                {
                    throw new RpcException(new Status(Grpc.Core.StatusCode.Internal, "Request Body Empty. (Using StudentsController)"));
                }

                MessageParser<U> parser = new MessageParser<U>(() => new U());
                return parser.ParseJson(json);
            }
            catch (Google.Protobuf.InvalidJsonException ex)
            {
                throw new RpcException(new Status(Grpc.Core.StatusCode.Internal, "Request Body Empty. (Using StudentsController)" + ex.Message));
            }

        }
    }

    private bool IsJsonObjectEmpty(string json)
    {
        bool isEmpty = false;

        try
        {
            var jsonDocument = JsonDocument.Parse(json);
            var jsonElement = jsonDocument.RootElement;

            var items = jsonElement.EnumerateObject();

            if (items.Count() <= 0)
            {
                isEmpty = true;
            }
        }
        catch (JsonException)
        {
            isEmpty = true;
        }
        catch (InvalidOperationException)
        {
            isEmpty = true;
        }

        return isEmpty;
    }
}

