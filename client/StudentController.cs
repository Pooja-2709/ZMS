using Google.Protobuf;
using Grpc.Core;
using Grpc.Net.Client;
using GrpcClient;
using Microsoft.AspNetCore.Mvc;
using System.Text;
using System.Text.Json;

namespace Controller.Students;

[Route("api/controller")]
public class StudentsController : ControllerBase
{
    private readonly GrpcChannel channel;
    private readonly Student.StudentClient client;
    public StudentsController()
    {
        channel = GrpcChannel.ForAddress("http://localhost:50051");
        client = new Student.StudentClient(channel);
    }

    [HttpPost("create")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> Create()
    {

        var request = await CreateProtobufMessage<CreateRequest>(Request.Body);
        var response = await client.createAsync(request);
        return Ok(response);
    }

    [HttpGet("read")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> Read()
    {
        var request = await CreateProtobufMessage<ReadRequest>(Request.Body);
        var response = await client.readAsync(request);
        return Ok(response);
    }

    [HttpGet("readall")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> ReadAll()
    {
        var request = await CreateProtobufMessage<ReadAllRequest>(Request.Body);
        var response = await client.readallAsync(request);
        return Ok(response);
    }



    [HttpDelete("delete")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> delete()
    {
        var request = await CreateProtobufMessage<DeleteRequest>(Request.Body);
        var response = await client.deleteAsync(request);
        return Ok(response);
    }



    [HttpPut("update")]
    [ProducesResponseType(StatusCodes.Status200OK)]
    [ProducesResponseType(StatusCodes.Status204NoContent)]
    [ProducesResponseType(StatusCodes.Status400BadRequest)]
    [ProducesResponseType(StatusCodes.Status404NotFound)]
    public async Task<IActionResult> update()
    {
        var request = await CreateProtobufMessage<UpdateRequest>(Request.Body);
        var response = await client.updateAsync(request);
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